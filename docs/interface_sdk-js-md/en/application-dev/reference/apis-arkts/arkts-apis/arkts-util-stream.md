# @ohos.util.stream

The stream module provides APIs to process basic types of streams. With streams, data is read or written by chunk,instead of being loaded to the memory at a time.There are four fundamental stream types: writable streams ([Writable]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_), readable streams (  
[Readable]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_), duplex streams ([Duplex]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_), and transform streams (  
[Transform]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace stream--><!--Device-unnamed-declare namespace stream-End-->

**System capability:** SystemCapability.Utils.Lang

## Summary

### Classes

| Name | Description |
| --- | --- |
| [Duplex](arkts-arkts-stream-duplex-c.md) | A stream that is both readable and writable. A duplex stream allows data to be transmitted in two directions, that is, data can be read and written.The **Duplex** class inherits from [Readable]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and supports all the APIs in  **Readable**. |
| [Readable](arkts-arkts-stream-readable-c.md) | Stream from which data can be read. A readable stream is used to read data from a source, such as a file or a network socket. |
| [Transform](arkts-arkts-stream-transform-c.md) | A special duplex stream that supports data conversion and result output. The **Transform** class inherits from  [Duplex]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and supports all the APIs in **Duplex**. |
| [Writable](arkts-arkts-stream-writable-c.md) | Stream to which data can be written. A writable stream allows data to be written to a target, which can be a file,an HTTP response, a standard output, another stream, or the like. |

### Interfaces

| Name | Description |
| --- | --- |
| [ReadableOptions](arkts-arkts-stream-readableoptions-i.md) | Describes the options used in the **Readable** constructor. |

