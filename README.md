# Upload Image To SM.MS By Automator

Drag your image to me, I will upload it to SM.MS automatically and backup info to iCloud. [Download Link](https://github.com/acbetter/upload-image-to-smms-by-automator/releases) [下载](https://github.com/acbetter/upload-image-to-smms-by-automator/releases)

## How to Use?

![Just Drag it!](https://i.loli.net/2018/04/23/5addef9892562.gif)

## Todo List

- [x] 🎉 Drag images and backup to iCloud
- [ ] 🤔 Drag images and backup to Dropbox
- [ ] 🤔 Drag images to remove automatic from SM.MS and Local (iCloud or Dropbox)
- [ ] 🤔 Upload image from copyboard and backup to iCloud
- [ ] 🤔 Upload image from copyboard and backup to Dropbox
- [ ] 🤔 Design icon

## Questions & Answer

1.  When I select many images and drag them into the app, which image's url will be copied into clipboard? 

- Answer: Because the app uploads images concurrencily, the app can't decide this. All the urls of images which have been uploaded will be copied into clipboard by order, so the result usually is that your clipboard have the url of the last image uploaded. You can use clipboard record software to check, such as Alfred, iPaste and so on.
    
    
2.  What should I do if I really want to upload many images at once?

- Answer: You can place your images in one folder and drag the folder into the app. All the urls of images will be copide into your clipboard, one url for one line.

3.  The application "Upload Images to SM.MS" can't be opened?

- Answer: Please open "Terminal.app" and run this command `sudo spctl --master-disable` then input your password. The reason is that the app hadn't been signed by my apple develop id. ~~I will signed the app later.~~

## LICENSE

MIT.
