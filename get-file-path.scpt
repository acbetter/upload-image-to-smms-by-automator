on isDirectory(thePOSIXPath)
	set theFileType to (do shell script "file -b " & thePOSIXPath)
	if theFileType ends with "directory" then return true
	return false
end isDirectory

on isImage(thePOSIXPath)
	if thePOSIXPath ends with ".jpeg" then
		return true
	else if thePOSIXPath ends with ".jpg" then
		return true
	else if thePOSIXPath ends with ".png" then
		return true
	else if thePOSIXPath ends with ".gif" then
		return true
	else if thePOSIXPath ends with ".bmp" then
		return true
	end if
	return false
end isImage

on actionGetFilePaths(inputFileList)
	set theFileList to {}
	repeat with theInputFileItem in inputFileList
		set theInputFilePath to theInputFileItem as string
		set theInputFilePOSIXPath to (the POSIX path of theInputFilePath)
		if isDirectory(theInputFilePOSIXPath) is true then
			-- list the files of the directory and find images...
			tell application "Finder"
				set theFileListDir to list folder theInputFileItem
			end tell
			repeat with theFileListDirItem in theFileListDir
				if isImage(theFileListDirItem) is true then
					-- add the image to the list waiting for handling...
					set end of theFileList to theInputFilePOSIXPath & theFileListDirItem
				end if
			end repeat
		else if isImage(theInputFilePOSIXPath) is true then
			set end of theFileList to theInputFilePOSIXPath
		end if
	end repeat
	return theFileList
end actionGetFilePaths

on actionGetFileNames(theFileList)
	set theFileNameList to {}
	repeat with theFileListItem in theFileList
		tell application "Finder"
			set theFileName to name of (POSIX file ("" & theFileListItem) as alias)
			set end of theFileNameList to theFileName
		end tell
	end repeat
	return theFileNameList
end actionGetFileNames

on actionListAsString(theList)
	set {TID, text item delimiters} to {text item delimiters, ", "}
	set theListAsString to theList as text
	set text item delimiters to TID
	return theListAsString
end actionListAsString

on run {input, parameters}
	set theFileList to actionGetFilePaths(input)
	set theFileNameList to actionGetFileNames(theFileList)
	display notification actionListAsString(theFileNameList) with title "🚀 Successfully Found " & (count of theFileList) & " Image(s)!" subtitle "All Images will be uploaded."
	return theFileList
end run
