# Tool

本模块定义的工具类，仅提供静态的方法，主要完成其他模块和[common2D](arkts-graphics-common2d.md#common2D)中定义的数据结构的转换功能。

> **说明：**
> 
> - 本Class首批接口从API version 15开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-drawing-class Tool--><!--Device-drawing-class Tool-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color
```

将ResourceColor类型的值转换为common2D.Color对象。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceColor | ResourceColor | 是 | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供10个示例输入）。其中第4种类型 [Resource](Resource)只接受``\\$r('belonging.type.name')``构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支 持color、string和integer，sys只支持color)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color | 转换后的common2D.Color颜色对象，若转换失败则返回undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined
```

将ResourceColor类型的值转换为common2D.Color对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceColor | ResourceColor | 是 | ResourceColor格式的颜色值（支持所有的4种输入，示例中提供10个示例输入）。其中第4种类型 [Resource](Resource)只接受``\\$r('belonging.type.name')``构造方法，需要确保该资源在main/resources/base/element目录下已定义(app支 持color、string和integer，sys只支持color)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common2D.Color | 转换后的common2D.Color颜色对象，若转换失败则返回undefined。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

