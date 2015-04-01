library(shiny)
library(boot)
library(tidyr)

shinyServer(function(input, output){
  
  Data <- reactive({
    inFile <- input$file1
    
    if (is.null(inFile))
      return (NULL)
    
    df <- read.csv(inFile$datapath, header=TRUE)
    return(df)
  })
  
  output$varx = renderUI({
    if (is.null(input$file1)) { return() }
    selectInput('varx', 'Variable 1', names(Data()))
  })

  output$vary = renderUI({
    if (is.null(input$file1)) { return() }
    selectInput('vary', 'Variable 2', names(Data()))
  })
  
  output$summary <- renderPrint({
    if (is.null(input$file1)) { return() }
    summary(Data()[,c(input$varx)])
  })
  
  output$distPlot <- renderPlot({
    
    if (is.null(input$file1)) { return() }
    if (!(input$varx %in% names(Data()))){ return() }

    if (input$statistic=="Mean"){
      Samples <- boot(Data(),function(x,id){return(mean(x[id,c(input$varx)],na.rm=T))},input$Samples)
      TitleA=paste("Bootstrapped samples of ",input$varx," mean\n")
    }
    if (input$statistic=="Correlation"){
      Samples <- boot(Data(),function(x,id){return(cor(x[id,c(input$varx)],x[id,c(input$vary)],use="pairwise.complete.obs"))},input$Samples)
      TitleA=paste("Bootstrapped samples of correlation between",input$varx,"and",input$vary,"\n")
    }
    if (input$statistic=="Mean difference"){
      Samples <- boot(Data(),function(x,id){return(mean(x[id,c(input$varx)],na.rm=T)-mean(x[id,c(input$vary)],na.rm=T))},input$Samples)
      TitleA=paste("Bootstrapped samples of mean difference between",input$varx,"and",input$vary,"\n")
    }
    res = boot.ci(Samples,type="basic")$basic
    lower = res[4]
    upper = res[5]
    hist(Samples$t, breaks = input$bins, col = 'skyblue', border = 'white',
         xlab="Statistic",ylab="Number of samples",
         main=paste(TitleA,"95% CI: ( ",lower," , ",upper," )"))
  })
})