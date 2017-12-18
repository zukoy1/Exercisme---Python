
How it Works: For New Developers

Using Exercism requires three tools:

    Your text editor: Write a solution to an exercise using your favorite text editor.
    Your command line interface: Fetch problems and submit solutions via the command line (or terminal).
    The exercism.io website: Review feedback on your solution and discuss it with other learners on the website.

For each exercise that you do, you'll go through the same basic steps.

    Fetch the exercise using the command line.
    Write code to solve the exercise on your own computer, satisfying each of the tests.
    Submit your solution using the command line. If you get stuck, submit what you have and ask for help. You also get to see other people's solutions to the same problem, which could help you figure it out.
    Review feedback and look at how other people solved the same problem on the website. Ask questions about what seems interesting or confusing!
    Improve your solution and resubmit as many times as desired.

You'll see many references to Command-Line Client, Command-Line Interface and CLI. These all mean the same thing. They are generic terms for programs/tools that are meant to be used on the command-line.

If the command-line feels foreign and intimidating to you, go work through the excellent Learn Enough™ Command-Line to be Dangerous tutorial by Michael Hartl.

As soon as you've submitted your first solution to an exercise, the next exercise becomes available via the command-line client.

Ready to get started? The following sections will detail how to get set up, including how to install the CLI, or Command Line Interface.
Creating an Account

To use Exercism, you first need an account.

We use GitHub for signup and login. This is just so we don't have to implement all the password-y stuff ourselves. It also gives us a username and avatar for you.

We only get public data, and we don't have access to change anything in your GitHub account.

GitHub is a professional social network that makes it easy for programmers to collaborate on software projects. It's free to use if you make all your code accessible publicly.
Installing the Command-Line Client

How you install the Exercism CLI depends on what kind of computer you have. We've explained all of this in detail on the installation page.

Installing the Command Line Interface

If you end up having to install the CLI manually, make sure to check out the video tutorial for your platform. If you're on Linux, it's similar enough to the Mac one that you could watch that.
Configuring the CLI

Once you have the CLI installed, you need to configure it. There are two reasons for this:

    When you fetch new exercises, we check which exercises you've already submitted in order to decide what to give you next.
    When you submit, we need to attach the solution to your account.

Since you're logged in you can just copy and paste this command:

1

	

exercism configure --key=46ad5fd3fb13408abe68fa2663a5151e

You can always find your API key in your account if you need it.

API stands for Application Programmer's Interface. Exercism has an API, which is kind of like a separate website without any HTML. Instead it returns more structured output making it easier to deal with programmatically.
Choosing a Language

Choose one of the available languages, then give exercism the fetch command.

For example, if you want to do the Python track, the fetch command is:

1

	

exercism fetch python

Some common "starter" languages are:

    Python
    Ruby
    Java
    JavaScript

Working the Exercises

Each exercise comes in the form of a README, which (as the name suggests) you should read, and an automated test suite, which simulates Test-Driven Development.

The README explains the basic idea of the exercise, but it doesn't necessarily list all of the details and constraints. It might also have some hints or links or other interesting references.

The automated test suite is what tells you exactly what your solution needs to do.

If you've never done TDD before it might take a little bit of getting used to. Each language will do this slightly differently, but the main idea is that the test calls your solution and checks that the result is what it expects.

Try to make one test pass at a time, without thinking ahead at what the next tests are going to ask for.

Once you've gotten all of the tests passing, you're good to go. Submit the solution to the site using the CLI. If you get stuck on a problem, feel free to submit incomplete code. Then check out other people's solutions and iterate/improve on your own. Re-submit a new iteration at any time.
