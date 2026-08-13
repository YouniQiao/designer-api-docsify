# OnLoadInterceptCallback

```TypeScript
export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean
```

当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean--><!--Device-unnamed-export type OnLoadInterceptCallback = (event: OnLoadInterceptEvent) => boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnLoadInterceptEvent](arkts-arkui-atomicservice-atomicserviceweb-onloadinterceptevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
