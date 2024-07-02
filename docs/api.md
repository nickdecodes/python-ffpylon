# API Reference
## Class: IOUtil

The `IOUtil` class provides utility methods for input/output operations.

### Method: get_logger

Returns a configured logger instance.

#### Parameters:
- `log_file` (str, optional): The name of the file to log to. If not provided, logging will be directed to the terminal.

#### Returns:
- `logging.Logger`: A configured logger instance.

#### Description:
This method retrieves or creates a logger instance based on the provided `log_file` argument. If no `log_file` is specified, a default logger named 'default_logger' is used. The method configures the logger with the specified log format and log level. If logging to a file, it uses rotation at midnight and keeps up to 7 backup log files.

If the logger does not already have handlers, the method configures the appropriate handler (either for logging to the terminal or to a file) and sets the formatter and log level for the handler. The configured logger is then returned.

#### Example Usage:
```python
# To obtain a logger logging to a file:
logger = IOUtil.get_logger('app.log')

# To obtain a logger logging to the terminal:
logger = IOUtil.get_logger()
```
