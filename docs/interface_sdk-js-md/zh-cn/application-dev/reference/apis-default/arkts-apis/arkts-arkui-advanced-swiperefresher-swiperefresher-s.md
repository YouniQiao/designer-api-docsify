# SwipeRefresher

内容加载指获取内容并加载出来，常用于衔接展示下拉加载的内容。主要用于实现下拉刷新功能。当用户下拉页面时，会触发内容加载操作，即从数据源获取新内容并动态展示在界面中。设备行为差异：该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

> **说明：**&gt;
> - 如果SwipeRefresher设置通用属性和通用事件，编译工具链会额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到SwipeRefresher本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SwipeRefresher设置通用属性和通用事件。
@struct { SwipeRefresher }

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Component

<!--Device-unnamed-export declare struct SwipeRefresher--><!--Device-unnamed-export declare struct SwipeRefresher-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SwipeRefresher-@Builder    build(): void--><!--Device-SwipeRefresher-@Builder    build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

内容加载时显示的文本。<br/>默认值：空字符串。<br/>**说明：**如果文本大于列宽时，文本被截断。

**类型：** ResourceStr

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SwipeRefresher-@PropRef    content?: ResourceStr--><!--Device-SwipeRefresher-@PropRef    content?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isLoading

```TypeScript
isLoading: boolean
```

当前是否正在加载。<br> true：正在加载。<br> false：未在加载。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @PropRef

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SwipeRefresher-@PropRef    isLoading: boolean--><!--Device-SwipeRefresher-@PropRef    isLoading: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

