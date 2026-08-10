# _rawfile

## _rawfile

```TypeScript
export declare function _rawfile(
    id: long, type: long, bundleName: string, moduleName: string, ...params: Object[]): Resource
```

Obtain the resource in resources/rawfile, used by plugin.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function _rawfile(    id: long, type: long, bundleName: string, moduleName: string, ...params: Object[]): Resource--><!--Device-unnamed-export declare function _rawfile(    id: long, type: long, bundleName: string, moduleName: string, ...params: Object[]): Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | long | 是 | Indicates the id of resource. |
| type | long | 是 | Indicates the type of resource. |
| bundleName | string | 是 | Indicates the name of bundle. |
| moduleName | string | 是 | Indicates the name of module. |
| params | Object[] | 是 | Custom parameters. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Resource](arkts-arkui-resource-t.md) | Returns the resource instance. |

