# File

Represents the file data. It is a child class of [UnifiedRecord]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and a base class of the data of the file type. You are advised to use the child class of **File**, for example, [Image]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [Video]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, and [Folder]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, to describe data.

**Inheritance/Implementation:** File extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class File extends UnifiedRecord--><!--Device-unifiedDataChannel-class File extends UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## details

```TypeScript
details?: Record<string, string>
```

A dictionary type object, where both the key and value are of the string type and are used to describe file information. For example, a data object with the following content can be created to describe a file: { "name":"File name", "type":"File type" } The default value is an empty dictionary object.

**Type:** Record&lt;string, string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-details?: Record<string, string>--><!--Device-File-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uri

```TypeScript
set uri(value: string)
```

Indicates the uri of file

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-File-set uri(value: string)--><!--Device-File-set uri(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uriAuthorizationPolicies

```TypeScript
set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)
```

Defines URI authorization policies for drag intention.

**Type:** Array&lt;UriPermission&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-File-set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)--><!--Device-File-set uriAuthorizationPolicies(value: Array<UriPermission> | undefined)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

