# File

Represents the file data. It is a child class of [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md#unifiedrecord) and a base class of the data of the file type. You are advised to use the child class of **File**, for example, [Image](arkts-arkdata-unifieddatachannel-image-c.md#image), [Video](arkts-arkdata-unifieddatachannel-video-c.md#video), and [Folder](arkts-arkdata-unifieddatachannel-folder-c.md#folder), to describe data.

**Inheritance/Implementation:** File extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md#unifiedrecord)

**Since:** 23

<!--Device-unifiedDataChannel-class File--><!--Device-unifiedDataChannel-class File-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
```

## details

```TypeScript
details?: Record<string, string>
```

A dictionary type object, where both the key and value are of the string type and are used to describe file information. For example, a data object with the following content can be created to describe a file: { "name":"File name", "type":"File type" } The default value is an empty dictionary object.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string&gt;

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-details?: Record<string, string>--><!--Device-File-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core
