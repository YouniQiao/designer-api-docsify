# TabBarOptions

Array of tab bar container configurations.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceTabs, TabBarOptions, TabBarPosition, TabContentBuilder, OnContentWillChangeCallback } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,
    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)
```

A constructor used to create a **TabBarOptions** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| icon | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [TabBarSymbol](../arkts-components/arkts-arkui-tabbarsymbol-c.md) | Yes |
| text | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes |
| unselectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | No |
| selectedColor | [ResourceColor](arkts-arkui-resourcecolor-t.md) | No |
