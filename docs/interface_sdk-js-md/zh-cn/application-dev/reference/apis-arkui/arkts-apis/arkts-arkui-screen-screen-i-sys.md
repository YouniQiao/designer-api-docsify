# Screen（系统接口）

[物理屏](../../../displaymanager/display-terminology.md#物理屏)屏幕实例。下列API示例中都需先使用[getAllScreens()](arkts-arkui-screen-getallscreens-f-sys.md)、 [createVirtualScreen()](arkts-arkui-screen-createvirtualscreen-f-sys.md) 中的任一方法获取到Screen实例，再通过此实例调用对应方法。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## setDensityDpi

```TypeScript
setDensityDpi(densityDpi: number, callback: AsyncCallback<void>): void
```

设置屏幕的像素密度，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| densityDpi | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## setDensityDpi

```TypeScript
setDensityDpi(densityDpi: number): Promise<void>
```

设置屏幕的像素密度，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| densityDpi | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## setOrientation

```TypeScript
setOrientation(orientation: Orientation, callback: AsyncCallback<void>): void
```

设置屏幕方向，使用callback异步回调。当设置的方向符合[应用旋转策略](../../../quick-start/module-configuration-file.md#abilities标签)（可通过配置 module.json5文件中abilities标签的orientation字段设置应用旋转策略）时，屏幕方向才会发生改变；当设置方向不符合应用旋转策略时，屏幕方向不会发生变化，且接口不会抛异常。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [orientation](#orientation) | [Orientation](#orientation) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## setOrientation

```TypeScript
setOrientation(orientation: Orientation): Promise<void>
```

设置屏幕方向，使用Promise异步回调。当设置的方向符合[应用旋转策略](../../../quick-start/module-configuration-file.md#abilities标签)（可通过配置 module.json5文件中abilities标签的orientation字段设置应用旋转策略）时，屏幕方向才会发生改变；当设置方向不符合应用旋转策略时，屏幕方向不会发生变化，且接口不会抛异常。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [orientation](#orientation) | [Orientation](#orientation) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## setOrientation

```TypeScript
setOrientation(orientation: Orientation, orientationOptions?: OrientationOptions): Promise<void>
```

设置屏幕方向

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [orientation](#orientation) | [Orientation](#orientation) | 是 |
| orientationOptions | [OrientationOptions](arkts-arkui-screen-orientationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## setScreenActiveMode

```TypeScript
setScreenActiveMode(modeIndex: number, callback: AsyncCallback<void>): void
```

设置屏幕当前显示模式，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modeIndex | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## setScreenActiveMode

```TypeScript
setScreenActiveMode(modeIndex: number): Promise<void>
```

设置屏幕当前显示模式，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modeIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## activeModeIndex

```TypeScript
readonly activeModeIndex: number
```

当前屏幕所处模式索引。模式索引的当前值和值的范围，会根据屏幕当前分辨率、刷新率和设备硬件差异产生变化。该参数为整数。

**类型：** number

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## id

```TypeScript
readonly id: number
```

屏幕的id，该参数应为整数。

**类型：** number

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## orientation

```TypeScript
readonly orientation: Orientation
```

屏幕方向。

**类型：** Orientation

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## parent

```TypeScript
readonly parent: number
```

屏幕所属群组的id，该参数为整数。

**类型：** number

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## rsId

```TypeScript
readonly rsId: number
```

屏幕端口的id，该参数为整数。

**类型：** number

**起始版本：** 21

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## screenType

```TypeScript
readonly screenType?: ScreenType
```

屏幕类型。

**类型：** [ScreenType](arkts-arkui-screen-screentype-e-sys.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

## serialNumber

```TypeScript
readonly serialNumber?: string
```

扩展屏幕的序列号，默认返回为空字符串。

**类型：** string

**起始版本：** 15

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## sourceMode

```TypeScript
readonly sourceMode: ScreenSourceMode
```

屏幕来源模式。

**类型：** [ScreenSourceMode](arkts-arkui-screen-screensourcemode-e-sys.md)

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## supportedModeInfo

```TypeScript
readonly supportedModeInfo: Array<ScreenModeInfo>
```

屏幕支持的模式集合。

**类型：** Array&lt;[ScreenModeInfo](arkts-arkui-screen-screenmodeinfo-i-sys.md)&gt;

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。
