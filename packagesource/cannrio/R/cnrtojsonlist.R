#' Convert an R object to an R list that can be returned to Plumber.
#'
#' Converts an R object to an R list that Plumber can then convert to JSON.
#' The output returned by Plumber is then of the form '{"data": <output data>}', e.g.,
#' '{"data": [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]}'
#' would be the output from a data frame with columns a, b, and c, and two rows.
#' If an error occurs during processing, the resulting output from Plumber would be of the form
#' {"error": <Error message>}'
#'
#' @param outputObject An R object
#' @param outputParseType A character string indicating how the output is to be converted.
#' Possible values are 'default' and 'none'.  'default' converts the output to a list.
#' 'none' converts the output to a quoted string.
#' @export
cnrToJSONList <- function(outputObject, outputParseType = 'default') {

  tryCatch(
    {
      if (outputParseType=='default') {
		    return(list("data" = outputObject))
      }
      else
        return(list("data" = toString(outputObject)))
    },
    error=function(cond) {
      # Return the error message
      return(list("error" = conditionMessage(cond)))
    }
  )

}
