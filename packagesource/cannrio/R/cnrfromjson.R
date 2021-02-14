#' Convert JSON input to a CANNR service to an R object
#'
#' Converts a JSON string to an R object.  This is a wrapper around the jsonlite
#' fromJSON function.  In the future, this function may enable the user to specify
#' additional information about how the input should be parsed.
#'
#' @param inputJSON A JSON string containing the data to be converted to an R object.
#' Must be of the form '{"data": <input data>}', e.g.,
#' '{"data": [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 5, "c": 6}]}'
#' will output a data frame with columns a, b, and c, and two rows.
#' @param inputParseType A character string indicating how the input is to be parsed.
#' @export
cnrFromJSON <- function(inputJSON, inputParseType = 'default') {

  # Get the input type
  inputType <- if (inputParseType == 'default') inputParseType else 'none'

  # Test that the input isn't empty
  if (length(inputJSON) == 0)
    rlang::abort('Input is empty')

  # Parse the input and check that element "data" exists
  inputList <- jsonlite::fromJSON(inputJSON)
  if (!exists("data", inputList))
    rlang::abort('Input element "data" is missing')

  # Return the data object
  return(inputList$data)

}

