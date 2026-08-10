# PasteDataProperty

定义剪贴板中所有内容条目的属性，包含时间戳、数据类型、粘贴范围以及一些附加数据等，该属性必须通过[setProperty](arkts-basicservices-pasteboard-pastedata-i.md#setproperty)方法，才能设置到剪贴板中。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-pasteboard-interface PasteDataProperty--><!--Device-pasteboard-interface PasteDataProperty-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## additions

```TypeScript
additions: Record<string, object>
```

设置其他附加属性数据。不支持动态追加属性，只能通过重新赋值的方式修改附加值，具体见相关示例setProperty， 默认为空。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, object&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-additions: Record<string, object>--><!--Device-PasteDataProperty-additions: Record<string, object>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## localOnly

```TypeScript
localOnly: boolean
```

配置剪贴板内容是否为“仅在本地”，true表示仅在本地有效，false表示允许跨设备传输。默认值为false。其值会被shareOption属性覆盖，推荐使用[ShareOption](arkts-basicservices-pasteboard-shareoption-e.md)属性。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-localOnly: boolean--><!--Device-PasteDataProperty-localOnly: boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## mimeTypes

```TypeScript
readonly mimeTypes: Array<string>
```

剪贴板内容条目的数据类型，非重复的类型列表。

**Type:** Array&lt;string&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-readonly mimeTypes: Array<string>--><!--Device-PasteDataProperty-readonly mimeTypes: Array<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## shareOption

```TypeScript
shareOption: ShareOption
```

指示剪贴板数据可以粘贴到的范围，默认值为CROSSDEVICE。与localOnly属性互斥，设置shareOption会影响localOnly的实际值。

**Type:** [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-shareOption: ShareOption--><!--Device-PasteDataProperty-shareOption: ShareOption-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## tag

```TypeScript
tag: string
```

用户自定义标签，默认为空。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-tag: string--><!--Device-PasteDataProperty-tag: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## timestamp

```TypeScript
readonly timestamp: long
```

剪贴板数据的写入时间戳（单位：已开机时间的ns数）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-readonly timestamp: long--><!--Device-PasteDataProperty-readonly timestamp: long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

