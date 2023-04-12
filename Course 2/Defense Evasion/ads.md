Hello and welcome to this
course in which we're talking about using Python
for defense evasion. In this video, we're going
to talk about the use of alternate data streams to
hide artifacts on a system. If you're not familiar, alternate data streams are streams of data,
as name suggests, that are associated with a file, but aren't precisely visible or at least easily visible
on the file system. They're built into
one particular file, but many of the different
tools that we could use to look at a particular
file's contents, we'll see it or execute
it on the terminal, etc don't actually
acknowledge these. For an example of this, in our Python code here where we're going to be working
with alternate data streams are decoy file or the benign
file that we're going to be hiding additional content
in is called benign.txt. We've got a copy of
that right over here, which simply says this
is a benign file. Notice that if you look at this, there's no additional
information associated with it. It's just a simple line of text. However, if we start
investigating this benign.txt, we see that there's a little
bit more hiding behind. Running a simple dir command in this directory reveals that
we have just two files. We have alternate
data streams dot pi, our Python file that we'll
be using to work with this benign.txt file and benign.txt. benign.txt size pretty
small, only 21. On the other hand, if we run dir slash r, which allows us to access and view alternate data streams, we see a very different story. We hit enter and we
see that we still have our benign.txt here, which has a size of 21. But behind it were actually
hiding three different files. We've got something
called commands dot text, which includes a command that can be run in the
windows command prompt. Something like a file less malware that's
living off the land. We've got something called
malicious.exe hidden in here. Notice that this thing size is much larger than
benign.txt appears. We have something called
result stuck text, which is designed to hide
it or hold configuration or output data from
running other commands. Despite the fact that
benign.txt appears to be just a single file on
the windows command line, there's actually a
lot hiding behind it. Many of the standard
windows terminal commands don't acknowledge the existence of this additional information. The type command allows you to print the contents of a file. If I type benign.txt, we again see the same text
that shows up over here. This is a benign file. Even if we know the name of one of those
alternate data streams that is hiding behind there. It says filename,
director name or volume labels syntax
is incorrect. It does not handle the colon properly and
you can't actually access the data stored in this alternate data stream using simple windows
terminal commands. However, the same is not true. Python, which is why we're including it in this
discussion of evading defenses because you could have a relatively benign
looking Python script that then accesses and uses functionality built into more malicious programs hidden using alternate data streams. Let's take a look at this file. We already know starting
out that we've got our benign decoy file
up front, benign.txt. If we look over in
our terminal results, we know that there
are three files hiding behind that
benign.txt file. What we have is a couple of files called command file
and result file, which are commands dot
text and results dot text. What we're going to
do with these in our Python script is
reading command file, iterate over the lines in
it, running those commands. Then putting the results
of executing them in result file or
results dot text. If you want to real
world use case for this, maybe you're attempting to collect data about
a user on a system. You might have a key logger
installed or have commands that can look for passwords
that are cached within browsers or other sensitive
data stored on the system. You don't want to send out this data continuously
when you find it, because if you do, then there's a chance that those transmissions might be detected. You want to build up a cache of data before
sending it out. However, you also don't
want this cache of sensitive information to be obviously stored on the system. Something like results
doc.txt which hides that information in
alternate data stream is a great choice
for hiding this. These three lines are where
we're going to actually take advantage of these
two data streams hidden behind benign.txt. I'm going to open
up a command file, iterate over it, and then
use the os.system command. We're going to run the
command on each line and then concatenate the result of
running it to result file. This allows us to run this multiple times and build up more
information over time, and then eventually we could
send out the contents of result file and then clear
it for storing future data, but we've also seen that we have a third alternate
data stream here. We have malicious.exe, and
so despite the fact that this particular
program is hiding in an alternate data
stream and it's not as easily found on
the file system, this doesn't mean that we can't access this alternate
data stream. All we need is the ability to properly provide its filename, similar to what we did up here with command
file and result file. What we use is a simple "BuildADSFilename"
function defined here at the top, which essentially
create the file name from the decoy file's name, so benign.txt colon
and then the text file or executable that we've stored in that
alternate data stream. So something like benign.txt
colon results.txt etc. If we build a proper
path for an executable, we can actually run
it on the system even though it's hidden in
an alternate data stream. We're going to use
os.path.join to get the current working
directory and then to build the proper
filename for that. We'll get something like C:\ users\hepos\downloads\benign.txt:malicious.exe. We then can use OS system to run WMIC process called
create and then provide the path to that
particular executable, and what this is going
do is it's going to run the executable stored within
this alternate data stream. If we attempt to run this code "python AlternateDataStreams.py"
and hit ''Enter'', a few things happen. The results here that we
are seeing are the results of executing the WMIC process
called create function. It's calling windows process "create" that attempts to run it, we get a process ID
and a return value. In fact back here, we see that it actually worked. In this case, our
malicious executable is just an instance of PuTTY, but we could easily have put something more dangerous or more malicious in that
malicious.exe file and use the alternate data stream to hide malware on the system. However, remember that running the executable is not
all that happened here. We also worked with our
command file and result file, and if we were on dir/ R, we see that something
did in fact happen. Earlier, we had a results
file size of zero, now we have 1 of 290. We've definitely got
some results here. However, if we try to access those results using
"type" as we saw before, this isn't going to work. It says incorrect syntax, but we can access and
view these results. We just need to use
good old notepad, so notepad benign.txt:
results.txt. We see that we've been collecting user account information for
this particular computer. We see the administrator
account, default, guest, hepos, and
WDAGUtility account. We're able to execute
what turns out to be net users account
successfully on the system, and we can confirm that this is the account or the
command that we were using using benign.txt
commands.txt in Notepad. We see net users. So we could easily modify this to include additional
commands and we just need to make sure that they'll
properly print their results to the alternate data
stream file results.txt. This demonstrates the
use of python with alternate data streams to
hide artifacts on a system. We can always use hidden files and folders
to hide artifacts, but those are fairly easy
to view because you can set Windows Explorer to
show hidden files and use the dir command
to see those as well. However, the only way to see alternate data streams and dir is to provide that slash R flag, which is intended, in fact, solely for displaying alternate
data streams of the file. You have to know that
alternate data streams exist and where to look for them to actually
identify them on the system, and that conclude this video where we're
demonstrating how to use alternate data streams to hide artifacts on the
system. Thank you.