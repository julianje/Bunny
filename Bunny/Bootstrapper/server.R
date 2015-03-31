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
  
  output$distPlot <- renderPlot({
    
    if (is.null(input$file1)) { return() }

    if (input$statistic=="Mean"){
      if (input$varx==""){ return() }
      Samples <- boot(Data(),function(x,id){return(mean(x[id,c(input$varx)]))},input$Samples)
    }
    if (input$statistic=="Correlation"){
      if (input$varx==""){ return() }
      if (input$vary==""){ return() }
      Samples <- boot(Data(),function(x,id){return(cor(x[id,c(input$varx)],x[id,c(input$vary)]))},input$Samples)
    }
    if (input$statistic=="Mean difference"){
      if (input$varx==""){ return() }
      if (input$vary==""){ return() }
      Samples <- boot(Data(),function(x,id){return(mean(x[id,c(input$varx)])-mean(x[id,c(input$vary)]))},input$Samples)
    }
    res = boot.ci(Samples)$basic
    lower = res[4]
    upper = res[5]
    # col = 'darkgray'
    hist(Samples$t, breaks = input$bins, col = 'skyblue', border = 'white',
         xlab="Statistic",ylab="Number of samples",
         main=paste("95% CI: ",lower," - ",upper))
  })
})