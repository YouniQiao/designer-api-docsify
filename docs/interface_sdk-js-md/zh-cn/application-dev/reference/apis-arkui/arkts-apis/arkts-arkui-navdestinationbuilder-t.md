# NavDestinationBuilder

```TypeScript
export type NavDestinationBuilder = (name: string, param?: Object) => void
```

NavDestination组件内容。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type NavDestinationBuilder = (name: string, param?: Object) => void--><!--Device-unnamed-export type NavDestinationBuilder = (name: string, param?: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面名称。  |
| param | Object | 否 | [NavDestination](../../apis-arkui/arkts-components/arkts-arkui-nav_destination-i)页面详细参数。默认值为空。  |

