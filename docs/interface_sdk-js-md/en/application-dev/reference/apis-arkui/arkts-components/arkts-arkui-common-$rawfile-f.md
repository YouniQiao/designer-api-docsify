# $rawfile

## $rawfile

```TypeScript
declare function $rawfile(value: string): Resource
```

global \$rawfile function

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-unnamed-declare function $rawfile(value: string): Resource--><!--Device-unnamed-declare function $rawfile(value: string): Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | name of the file in the resources/rawfile directory of the project. When referencing resources of the Resource type, make sure the data type is the same as that of the attribute method. For example, if an attribute method supports the string \| Resource types, the data type of the Resource type must be string. |

**Return value:**

| Type | Description |
| --- | --- |
| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) |  |

