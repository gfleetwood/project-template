"
Extract computations (less CPU usage):

https://appsilon.com/shiny-worker-package
https://rstudio.github.io/promises/articles/shiny.html

Caching:

https://shiny.rstudio.com/articles/caching.html
https://shiny.rstudio.com/articles/plot-caching.html

Leverage front end with js (less CPU usage):

https://appsilon.com/how-to-scale-a-shiny-dashboard/
https://book.javascript-for-r.com/
https://appsilon.com/r-shiny-faster-updateinput-css-javascript/
https://appsilon.com/super-solutions-for-shiny-architecture-2-javascript-is-your-friend/
https://js4shiny.com/resources/links/
https://connect.thinkr.fr/js4shinyfieldnotes/

observeEvent(input$print_button, {

  # Print all input widgets
  cat('Printing all input widgets:\n')

  for(name in names(input)) {
    cat(paste0(name, ": ", input[[name]], '\n''))
  }

})
"

library(tidyverse)
library(shiny)
library(reticulate)
library(glue)
library(shinythemes)
library(odbc)
library(DBI)
library(RSQLite)
library(logger)

con <- DBI::dbConnect(
  odbc::odbc(),
  Driver = "PostgreSQL ANSI", 
  Database = "",
  Port = "5432",
  Server = "",
  UID = "",
  PWD = "",
  sslmode = "require"
)

dbWriteTable(con, "bmf_index_cleaned", sample_n(bmf_index_cleaned, 100000), overwrite = TRUE)
dbWriteTable(con, "bmf_index_cleaned", bmf_index_cleaned, append = TRUE)

dbGetQuery(con, "SELECT * FROM bmf_index_cleaned limit 1")
dbListTables(con)


log_threshold(INFO)
log_appender(appender_file("log.log"))
log_info('Log')