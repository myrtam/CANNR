#' Convert an R object to JSON to be returned by a CANNR service
#'
#' Converts an R object to a JSON string to be output by a CANNR service.
#' The output is of the form '{"data": <output data>}', e.g.,
#' '{"data": [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]}'
#' would be the output from a data frame with columns a, b, and c, and two rows.
#'
#' @param outputObject An R object
#' @param outputParseType A character string indicating how the output is to be converted.
#' Possible values are 'default' and 'none'.  'default' converts the output using jsonlite
#' for non-atomic types and unbracketed values for atomic types.
#' 'none' converts the output to a quoted string.
#' @export
cnrToJSON <- function(outputObject, outputParseType = 'default') {

  tryCatch(
    {
      if (outputParseType=='default') {
		    return(list("data" = outputObject))
      }
      else
        #return(paste0('{"data": "', stringr::str_replace_all(toString(outputObject), pattern), '"}'))
        return(list("data" = toString(outputObject)))
    },
    error=function(cond) {
      # Return the error message
      return(list("error" = conditionMessage(cond)))
    }
  )

}

# Pattern to escape JSON special chars.
pattern <- c('\\\\' = '\\\\\\\\', "\'" = "\\\\'", '\b' = '\\\\b', '\f' = '\\\\f',
  '\n' = '\\\\n', '\r' = '\\\\r', '\t' = '\\\\t', '"' = '\\\\\"')
