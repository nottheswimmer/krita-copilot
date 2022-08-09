# Krita Copilot

Krita Copilot is a plugin for Krita that enables you to use DALL·E 2 from within Krita.


https://user-images.githubusercontent.com/29849378/183610010-ca7fc088-57d8-4d5f-a907-66809c305ef5.mp4



## Tips

- Get access by signing up for the [DALL·E 2 waitlist][1].

- Ensure your usage of DALL·E 2 abides by DALL·E 2's [content policy][2] and [terms of use][3].

- Be mindful about how easy this plugin makes it for you to spend your money / DALL·E 2 credits.

## Support

Krita has been tested on Windows. Linux and MacOS may be supported, but this has not been tested.

## Installation

### Install from URL

1. Open Krita
2. Go to "Tools" -> "Scripts" -> "Import Python Plugin from Web"
3. Paste the following URL into the text box:
   `https://github.com/nottheswimmer/krita-copilot`
4. Click "OK"
5. Click "Yes" when asked if you would like to enable the plugin
6. Restart Krita (close and reopen)

### Install from local file

1. Download the contents of this repository from GitHub
   1. Click the green "Code" button in the upper right corner
   2. Click "Download ZIP"
2. Open Krita
3. Go to "Settings" -> "Manage Resources" -> "Open Resource Folder"
4. Open pykrita
5. Extract the contents of the zip file into the "pykrita" folder

   If done correctly, the krita_copilot.desktop file and krita_copilot directory should be in the "pykrita" folder.
6. Restart Krita (close and reopen)
7. Go to "Settings" -> "Configure Krita"
8. Scroll down on the left until you see "Python Plugin Manager" and click it
9. Check boxes that say "Krita Copilot" - if there's two you can just click both.
10. Restart Krita (close and reopen)

### A successful installation

If installed correctly, you should see a "docker" in the bottom right called "Krita Copilot." It's possible that
you do everything correctly and the plugin is still not working. If you feel that this is the case, please open an 
issue on GitHub.

## Troubleshooting

- Q: I saw a very big error message, what do I do?

  A: Error messages aren't very user-friendly at the moment. Errors can happen due to a few reasons. Here's a list
     of the common reasons and what to do about them:
  - A Krita Copilot bug
    - File an issue.
  - A network error
    - Check your internet connection.
  - A DALL·E 2 server error
    - Wait for a little bit and try again.
  - A credential error
    - Check your username and password for OpenAI.
  - You don't have enough credits
    - Buy more credits or wait for a refresher.
  - A DALL·E 2 bug
    - Report it to the DALL·E 2 team.

- Q: Inpainting is just returning the original image, why is that?

  A: Your selection needs to contain transparency in order for that area to be inpainted.

- Q: The image pasted is larger than the region I selected, what gives?

  A: DALL·E 2 will only accept and output images that are squares. Currently, the rule used to resolve this is that
     the maximum of your selection's width/height is used as the side length of the square, and the full output image
     is pasted into the selected area from the top left corner. A future version could have a setting to allow you to
     automatically crop the output image to the selection's size.

## Technical Notes (for nerds)

- Krita Copilot was developed using [PyDalle](https://github.com/nottheswimmer/dalle), a library I created for using
  the DALL·E 2 API.
- Because Krita has no built-in support for third-party dependencies, the requirements are downloaded from pypi by a 
  script called dependencies.py and added to the PATH before they are imported. Those dependencies are stored in a
  directory where Krita also stores settings and downloaded images. The location of this directory varies by OS.

[1]: https://labs.openai.com/waitlist

[2]: https://labs.openai.com/policies/content-policy

[3]: https://labs.openai.com/policies/terms
