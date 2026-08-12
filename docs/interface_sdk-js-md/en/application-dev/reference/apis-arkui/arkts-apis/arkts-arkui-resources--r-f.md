# _r

## _r

```TypeScript
export declare function _r(
    id: long, type: long, bundleName: string, moduleName: string, ...params: Object[]): Resource
```

Obtain the resource in resources, used by plugin.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function _r(    id: long, type: long, bundleName: string, moduleName: string, ...params: Object[]): Resource--><!--Device-unnamed-export declare function _r(    id: long, type: long, bundleName: string, moduleName: string, ...params: Object[]): Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | long | Yes | Indicates the id of resource. |
| type | long | Yes | Indicates the type of resource. |
| bundleName | string | Yes | Indicates the name of bundle. |
| moduleName | string | Yes | Indicates the name of module. |
| params | Object[] | Yes | Custom parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Returns the resource instance. |

