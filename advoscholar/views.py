from django.http import HttpResponse


def view_logs(request):
    """
    View function that reads and displays the contents of a log file.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the log file content.

    Raises:
        FileNotFoundError: If the log file is not found.
    """
    log_file_path = "general.log"  # Adjust the path if the log file is located elsewhere

    try:
        with open(log_file_path, "r") as file:
            lines = file.readlines()
            lines.reverse()  # Reverse the order of lines
            content = ''.join(lines)  # Join the lines into a single string
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("Log file not found", content_type='text/plain')
