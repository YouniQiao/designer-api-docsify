# IsolatedComponentInterface（系统接口）

```TypeScript
declare type IsolatedComponentInterface = (options: IsolatedOptions) => IsolatedComponentAttribute
```

创建IsolatedComponent组件，用于显示受限Worker运行的Abc。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [IsolatedOptions](arkts-arkui-isolatedoptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [IsolatedComponentAttribute](arkts-arkui-isolatedcomponentattribute-c-sys.md) |
