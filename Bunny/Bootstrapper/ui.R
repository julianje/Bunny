library(shiny)

shinyUI(fluidPage(
  # Title
  img(src="BunnyLogo.png", align="center"),
  # Side bar
  sidebarLayout(
    sidebarPanel(
      fileInput('file1', 'Choose CSV File',
                accept=c('text/csv', 
                         'text/comma-separated-values,text/plain', 
                         '.csv')),
      textInput('varx', "Variable X", ""),
      textInput('vary', "Variable Y", ""),
      #selectInput('varx', 'Variable X', names(Data())),
      #selectInput('vary', 'Variable Y', names(Data())),
      selectInput('statistic', 'Statistic', c("Mean","Correlation","Mean difference")),
      numericInput('Samples','Number of samples', 10000, min=100, max=100000),
      sliderInput('bins','Number of bins:',
                  min=1,
                  max=50,
                  value=30)
      ),
    mainPanel(
      plotOutput("distPlot")
    )
  )
))