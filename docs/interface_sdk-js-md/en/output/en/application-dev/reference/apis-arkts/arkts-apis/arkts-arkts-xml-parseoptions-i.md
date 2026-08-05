# ParseOptions

Parse options for XmlPullParser.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-xml-interface ParseOptions--><!--Device-xml-interface ParseOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## attributeValueCallbackFunction

```TypeScript
attributeValueCallbackFunction?: (name: string, value: string) => boolean
```

Attribute value callback function.

**Type:** (name: string, value: string) =&gt; boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-attributeValueCallbackFunction?: (name: string, value: string) => boolean--><!--Device-ParseOptions-attributeValueCallbackFunction?: (name: string, value: string) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## attributeWithTagCallbackFunction

```TypeScript
attributeWithTagCallbackFunction?: AttributeWithTagCb
```

Attribute value and tag callback function.

**Type:** AttributeWithTagCb

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ParseOptions-attributeWithTagCallbackFunction?: AttributeWithTagCb--><!--Device-ParseOptions-attributeWithTagCallbackFunction?: AttributeWithTagCb-End-->

**System capability:** SystemCapability.Utils.Lang

## ignoreNameSpace

```TypeScript
ignoreNameSpace?: boolean
```

Whether to ignore parsing texts of the elements.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-ignoreNameSpace?: boolean--><!--Device-ParseOptions-ignoreNameSpace?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## supportDoctype

```TypeScript
supportDoctype?: boolean
```

Whether to parsing Doctype of the elements.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-supportDoctype?: boolean--><!--Device-ParseOptions-supportDoctype?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## tagValueCallbackFunction

```TypeScript
tagValueCallbackFunction?: (name: string, value: string) => boolean
```

Tag value callback function.

**Type:** (name: string, value: string) =&gt; boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-tagValueCallbackFunction?: (name: string, value: string) => boolean--><!--Device-ParseOptions-tagValueCallbackFunction?: (name: string, value: string) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## tokenValueCallbackFunction

```TypeScript
tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean
```

Token value callback function.

**Type:** (eventType: EventType, value: ParseInfo) =&gt; boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean--><!--Device-ParseOptions-tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

