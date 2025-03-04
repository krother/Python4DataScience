.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Undo changes
============

:samp:`$ git reset [--hard|--soft] {TARGET_REFERENCE}`
    resets the history to a previous commit, for example:

    .. code-block:: console

        $ git reset HEAD~1

    ``--HEAD~1``
        takes back the last commit and its changes are now transferred back to
        the staging area.

        If there are changes in the staging area, they are moved to the working
        area, for example:

        .. code-block:: console

            $ echo 'My first repo' > README.rst
            $ git add README.rst
            $ git status
            On branch main
            Changes marked for commit:
              (use "git rm --cached <Datei>..." to remove from staging area)
                New file:     README.rst
            $ git reset
            $ git status
            On branch main
            Unversioned files:
              (use "git add <file>...", to mark the changes for commit)
                README.rst

    ``--hard``
        discards the changes in the staging and working area as well.

        .. code-block:: console

            $ git status
            On branch main
            Changes marked for commit:
              (use "git rm --cached <Datei>..." to remove from staging area)
                New file:     README.rst
            $ git reset --hard
            $ git status
            On branch main
            nothing to commit (create/copy files and use "git add" to version)

    ``--soft``
        takes back the commits, but leaves the stage and workspace unchanged.

    .. warning::
        The risk with ``reset`` is that work can be lost. Commits are not
        deleted immediately, but they can become orphaned so that there is no
        direct path to them. They must then be found and restored promptly with
        ``git reflog``, as Git usually deletes all orphaned commits after 30
        days.

:samp:`$ git revert {COMMIT SHA}`
    creates a new commit and reverts the changes of the specified commit so that
    the changes are inverted.
:samp:`$ git fetch --prune {REMOTE}`
    Remote refs are removed when they are removed from the remote repository.
:samp:`$ git commit --amend`
    updates and replaces the last commit with a new commit that combines all
    deployed changes with the contents of the previous commit. If nothing is
    provided, only the previous commit message is rewritten.
:samp:`$ git restore {FILE}`
    changes files in the working directory to a state previously known to Git.
    By default, Git ``HEAD`` checks out the last commit of the current branch.

    .. note::

        In Git < 2.23, ``git restore`` is not yet available. In this case you
        still have to use ``git checkout``:

       :samp:`$ git checkout {FILE}`

If you have accidentally committed to an existing branch instead of creating a
new branch first, you can change this in the following three steps:

:samp:`$ git branch {NEW_BRANCH}`
    create a new branch
:samp:`$ git reset HEAD~ --hard`
     resets the last commit in your active branch
:samp:`$ git switch {NEW_BRANCH}`
    applies the changes to the new branch

The procedure is similar if you have accidentally made a commit in the wrong
branch:

:samp:`$ git reset HEAD~`
    resets the last commit, and its changes are now reapplied to the stage area.


.. _git-filter-repo:

Remove a file from the history
------------------------------

A file can be completely removed from the current branches Git history.
This could be necessary if you accidentally committed passwords or huge files:

.. code-block:: console

    $ git filter-repo --invert-paths --path path/somefile
    $ git push --no-verify --mirror

.. note::
    Inform the team members that they should create a clone of the
    repository again.

Remove a string from the history
--------------------------------

.. code-block:: console

    $ git filter-repo --message-callback 'return re.sub(b"^git-svn-id:.*\n", b"", message, flags=re.MULTILINE)'

.. seealso::
    * `git-filter-repo — Man Page <https://www.mankier.com/1/git-filter-repo>`_
    * `git-reflog <https://git-scm.com/docs/git-reflog>`_
    * `git-gc <https://git-scm.com/docs/git-gc>`_
