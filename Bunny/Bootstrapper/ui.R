library(shiny)

shinyUI(fluidPage(
  # Title
  HTML("<center>"),
  img(src="BunnyLogo.png"),
  HTML("</center>"),
  # Side bar
  sidebarLayout(
    sidebarPanel(
      h4("Usage"),
      p("Upload a csv file and choose two columns. Some statistics will use both columns; others only use the first one. Your data is deleted when you close the window."),
      HTML('<a href="https://github.com/julianje/Bunny/blob/master/Bunny/Bootstrapper/ExampleData.csv">Download an example file.</a>'),
      fileInput('file1', 'Choose CSV File',
                accept=c('text/csv', 
                         'text/comma-separated-values,text/plain', 
                         '.csv')),
      uiOutput("varx"),
      uiOutput("vary"),
      selectInput('statistic', 'Statistic', c("Mean","Correlation","Mean difference")),
      numericInput('Samples','Number of bootstrap samples', 1000, min=100, max=100000),
      sliderInput('bins','Adjust bins in plot',
                  min=1,
                  max=50,
                  value=30),
      HTML('Implemented by <a href="http://web.mit.edu/jjara/www/">Julian</a> and powered by R and shiny.')
      ),
    mainPanel(
      plotOutput("distPlot"),
      h2("Data summary of variable 1"),
      verbatimTextOutput("summary")
    )
  )
))