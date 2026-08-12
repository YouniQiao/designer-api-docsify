# SamplingOptions

采样选项对象，用于配置图像采样时的过滤模式，控制图像缩放或变换过程中的像素采样方式。典型使用场景为在Canvas上绘制图像（如drawImage）时，以不同过滤模式决定图像的采样质量与渲染效果。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

<!--Device-drawing-class SamplingOptions--><!--Device-drawing-class SamplingOptions-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor()
```

构造一个新的采样选项对象，[FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md#FilterMode)的默认值为FILTER_MODE_NEAREST。

**起始版本：** 12

<!--Device-SamplingOptions-constructor()--><!--Device-SamplingOptions-constructor()-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(filterMode: FilterMode)
```

构造一个新的采样选项对象，可通过指定filterMode参数适配不同的图像采样场景。

**起始版本：** 12

<!--Device-SamplingOptions-constructor(filterMode: FilterMode)--><!--Device-SamplingOptions-constructor(filterMode: FilterMode)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filterMode | [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
