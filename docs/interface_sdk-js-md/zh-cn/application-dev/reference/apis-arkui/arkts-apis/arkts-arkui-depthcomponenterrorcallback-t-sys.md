# DepthComponentErrorCallback（系统接口）

```TypeScript
export declare type DepthComponentErrorCallback = (error: DepthComponentErrorEvent) => void
```

背景资源加载失败的回调函数。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| error | [DepthComponentErrorEvent](arkts-arkui-depthcomponent-depthcomponenterrorevent-i-sys.md) | 是 |
