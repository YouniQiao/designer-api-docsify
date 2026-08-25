# TabBarOptions

页签选项。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AtomicServiceTabs, TabBarOptions, TabBarPosition, TabContentBuilder, OnContentWillChangeCallback } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,
    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)
```

TabBarOptions的构造函数。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | ResourceStr \| [TabBarSymbol](../arkts-components/arkts-arkui-tabbarsymbol-c.md) | 是 |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |
| unselectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 |
| selectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 |
