import re

def show_time_of_pid(line):
    # Define the pattern using regular expressions
    pattern = r"^(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) \w+ (\w+)\[([0-9]+)\]:"
    
    # Use re.search to find the pattern in the input line
    result = re.search(pattern, line)
    
    # Check if the pattern was found
    if result:
        # Replace '___' with the appropriate groups to construct the desired output
        return f"{result.group(1)} pid:{result.group(3)}"

# Test cases
print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))  # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))  # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))  # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))  # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))  # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))  # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))  # Jul 6 14:05:01 pid:29440
