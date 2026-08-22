# File

File

**Since:** 3

**Deprecated since:** 10

<!--Device-unnamed-export default class File--><!--Device-unnamed-export default class File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## Modules to Import

```TypeScript
```

## access

```TypeScript
static access(options: FileAccessOption): void
```

Checks whether a file or directory exists.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [access](arkts-corefile-file-fs-access-f.md)

<!--Device-File-static access(options: FileAccessOption): void--><!--Device-File-static access(options: FileAccessOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileAccessOption](arkts-corefile-system-file-fileaccessoption-depr-i.md) | Yes | Options for checking whether a file or directory exists. |

**Examples**

```TypeScript
export default {    
  access() {        
    file.access({            
      uri: 'internal://app/test',            
      success: function() {                
        console.info('call access success.');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },        
    });    
  }
}
```

## copy

```TypeScript
static copy(options: FileCopyOption): void
```

Copies a file to the given URI.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

<!--Device-File-static copy(options: FileCopyOption): void--><!--Device-File-static copy(options: FileCopyOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileCopyOption](arkts-corefile-system-file-filecopyoption-depr-i.md) | Yes | Options for copying the files. |

**Examples**

```TypeScript
export default {    
  copy() {        
    file.copy({            
      srcUri: 'internal://app/file.txt',            
      dstUri: 'internal://app/file_copy.txt',            
      success: function(uri) {                
        console.info('call success callback success');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## delete

```TypeScript
static delete(options: FileDeleteOption): void
```

Deletes a local file.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [unlink](arkts-corefile-file-fs-unlink-f.md)

<!--Device-File-static delete(options: FileDeleteOption): void--><!--Device-File-static delete(options: FileDeleteOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileDeleteOption](arkts-corefile-system-file-filedeleteoption-depr-i.md) | Yes | Options for deleting a local file. |

**Examples**

```TypeScript
export default {    
  delete() {        
    file.delete({            
      uri: 'internal://app/my_file',            
      success: function() {                
        console.info('call delete success.');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## get

```TypeScript
static get(options: FileGetOption): void
```

Obtains information about a local file.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [stat](arkts-corefile-file-fs-stat-f.md)

<!--Device-File-static get(options: FileGetOption): void--><!--Device-File-static get(options: FileGetOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileGetOption](arkts-corefile-system-file-filegetoption-depr-i.md) | Yes | Options for obtaining information about a local file. |

**Examples**

```TypeScript
export default {    
  get() {        
    file.get({            
      uri: 'internal://app/file',            
      success: function(data) {                
        console.info(data.uri);            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## list

```TypeScript
static list(options: FileListOption): void
```

Obtains all files in the specified directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

<!--Device-File-static list(options: FileListOption): void--><!--Device-File-static list(options: FileListOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileListOption](arkts-corefile-system-file-filelistoption-depr-i.md) | Yes | Options for obtaining all files in the specified directory. |

**Examples**

```TypeScript
export default {    
  list() {        
    file.list({            
      uri: 'internal://app/pic',            
      success: function(data) {                
        console.info(JSON.stringify(data.fileList));            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },        
    });    
  }
}
```

## mkdir

```TypeScript
static mkdir(options: FileMkdirOption): void
```

Creates a directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md)

<!--Device-File-static mkdir(options: FileMkdirOption): void--><!--Device-File-static mkdir(options: FileMkdirOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileMkdirOption](arkts-corefile-system-file-filemkdiroption-depr-i.md) | Yes | Options for creating a directory. |

**Examples**

```TypeScript
export default {    
  mkdir() {        
    file.mkdir({            
      uri: 'internal://app/test_directory',            
      success: function() {                
        console.info('call mkdir success.');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## move

```TypeScript
static move(options: FileMoveOption): void
```

Moves a specified file to a given location.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [moveFile](arkts-corefile-file-fs-movefile-f.md)

<!--Device-File-static move(options: FileMoveOption): void--><!--Device-File-static move(options: FileMoveOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileMoveOption](arkts-corefile-system-file-filemoveoption-depr-i.md) | Yes | Options for moving the files. |

**Examples**

```TypeScript
export default {    
  move() {        
    file.move({            
      srcUri: 'internal://app/myfiles1',            
      dstUri: 'internal://app/myfiles2',            
      success: function(uri) {                
        console.info('call success callback success');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },        
    });    
  }
}
```

## readArrayBuffer

```TypeScript
static readArrayBuffer(options: FileReadArrayBufferOption): void
```

Reads buffer data from a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [read](arkts-corefile-file-fs-read-f.md)

<!--Device-File-static readArrayBuffer(options: FileReadArrayBufferOption): void--><!--Device-File-static readArrayBuffer(options: FileReadArrayBufferOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileReadArrayBufferOption](arkts-corefile-system-file-filereadarraybufferoption-depr-i.md) | Yes | Options for reading buffer data from a file. |

**Examples**

```TypeScript
export default {    
  readArrayBuffer() {        
    file.readArrayBuffer({            
      uri: 'internal://app/test',            
      position: 10,            
      length: 200,            
      success: function(data) {                
        console.info('call readArrayBuffer success: ' + data.buffer);            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## readText

```TypeScript
static readText(options: FileReadTextOption): void
```

Reads text from a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [readText](arkts-corefile-file-fs-readtext-f.md)

<!--Device-File-static readText(options: FileReadTextOption): void--><!--Device-File-static readText(options: FileReadTextOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileReadTextOption](arkts-corefile-system-file-filereadtextoption-depr-i.md) | Yes | Options for reading text from a file. |

**Examples**

```TypeScript
export default {    
  readText() {        
    file.readText({            
      uri: 'internal://app/text.txt',            
      success: function(data) {                
        console.info('call readText success: ' + data.text);            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },        
    });    
  }
}
```

## rmdir

```TypeScript
static rmdir(options: FileRmdirOption): void
```

Deletes a directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [rmdir](arkts-corefile-file-fs-rmdir-f.md)

<!--Device-File-static rmdir(options: FileRmdirOption): void--><!--Device-File-static rmdir(options: FileRmdirOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileRmdirOption](arkts-corefile-system-file-filermdiroption-depr-i.md) | Yes | Options for deleting a directory. |

**Examples**

```TypeScript
export default {    
  rmdir() {        
    file.rmdir({            
      uri: 'internal://app/test_directory',            
      success: function() {                
        console.info('call rmdir success.');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## writeArrayBuffer

```TypeScript
static writeArrayBuffer(options: FileWriteArrayBufferOption): void
```

Writes buffer data into a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

<!--Device-File-static writeArrayBuffer(options: FileWriteArrayBufferOption): void--><!--Device-File-static writeArrayBuffer(options: FileWriteArrayBufferOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileWriteArrayBufferOption](arkts-corefile-system-file-filewritearraybufferoption-depr-i.md) | Yes | Options for writing buffer data into a file. |

**Examples**

```TypeScript
export default {    
  writeArrayBuffer() {       
    file.writeArrayBuffer({           
      uri: 'internal://app/test',           
      buffer: new Uint8Array(8),// The buffer is of the Uint8Array type.
      success: function() {                
        console.info('call writeArrayBuffer success.');            
      },           
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },
    });    
  }
}
```

## writeText

```TypeScript
static writeText(options: FileWriteTextOption): void
```

Writes text into a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

<!--Device-File-static writeText(options: FileWriteTextOption): void--><!--Device-File-static writeText(options: FileWriteTextOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileWriteTextOption](arkts-corefile-system-file-filewritetextoption-depr-i.md) | Yes | Options for writing text into a file. |

**Examples**

```TypeScript
export default {    
  writeText() {        
    file.writeText({            
      uri: 'internal://app/test.txt',            
      text: 'Text that just for test.',            
      success: function() {                
        console.info('call writeText success.');            
      },            
      fail: function(data, code) {                
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);            
      },        
    });    
  }
}
```

