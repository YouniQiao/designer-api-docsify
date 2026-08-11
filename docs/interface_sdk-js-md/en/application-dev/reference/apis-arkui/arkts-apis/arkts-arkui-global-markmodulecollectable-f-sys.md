# markModuleCollectable (System API)

## markModuleCollectable

```TypeScript
export declare function markModuleCollectable(namespace: Object): void
```

Mark moduleNamespace which loaded by dynamic-import is collectable.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function markModuleCollectable(namespace: Object): void--><!--Device-unnamed-export declare function markModuleCollectable(namespace: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| namespace | Object | Yes | moduleNamespace to be marked. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | if type of object is not moduleNameSpace. |

