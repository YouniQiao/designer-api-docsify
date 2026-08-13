# createIncrementalSource

## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer): ImageSource | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |


## createIncrementalSource

```TypeScript
function createIncrementalSource(buf: ArrayBuffer, 
      options?: SourceOptions): ImageSource | undefined
```

Creates an ImageSource instance based on the buffer in incremental.

**起始版本：** 23

**废弃版本：** -1

<!--Device-image-function createIncrementalSource(buf: ArrayBuffer,       options?: SourceOptions): ImageSource | undefined--><!--Device-image-function createIncrementalSource(buf: ArrayBuffer,       options?: SourceOptions): ImageSource | undefined-End-->

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buf | ArrayBuffer | 是 |
| options | [SourceOptions](arkts-image-image-sourceoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageSource](arkts-image-sendableimage-imagesource-i.md) |
