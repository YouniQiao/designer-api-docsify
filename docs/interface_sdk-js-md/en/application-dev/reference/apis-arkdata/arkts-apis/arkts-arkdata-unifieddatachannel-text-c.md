# Text

Represents the text data. It is a child class of [UnifiedRecord]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and a base class of text data. You are advised to use the child class of **Text**, for example,  
[PlainText]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [Hyperlink]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, and  
[HTML]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, to describe data.

**Inheritance/Implementation:** Text extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class Text extends UnifiedRecord--><!--Device-unifiedDataChannel-class Text extends UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## details

```TypeScript
details?: Record<string, string>
```

A dictionary type object, where both the key and value are of the string type and are used to describe the text content. For example, a data object with the following content can be created to describe a text file:

{

"title":"Title of the file",

"content":"Content of the file"

}

The default value is an empty dictionary object.

**Type:** Record&lt;string, string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Text-details?: Record<string, string>--><!--Device-Text-details?: Record<string, string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

