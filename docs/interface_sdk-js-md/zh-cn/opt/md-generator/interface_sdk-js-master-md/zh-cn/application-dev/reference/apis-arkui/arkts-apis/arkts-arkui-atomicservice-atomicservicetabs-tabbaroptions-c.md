# TabBarOptions

页签选项。

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-export declare class TabBarOptions--><!--Device-unnamed-export declare class TabBarOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,
    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)
```

TabBarOptions的构造函数。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TabBarOptions-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)--><!--Device-TabBarOptions-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| TabBarSymbol | 是 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |
| unselectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 |
| selectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 |
