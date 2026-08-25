# Aspect

Provides APIs that support Aspect Oriented Programming (AOP). These APIs can be used to perform instrumentation or replacement on class methods.

**Since:** 11

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## addAfter

```TypeScript
static addAfter(targetClass: Object, methodName: string, isStatic: boolean, after: Function): void
```

Inserts a function after a method of a class object. The final return value is the return value of the function inserted.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | Object | Yes |
| methodName | string | Yes |
| [isStatic](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutinfo-depr-i.md) | boolean | Yes |
| [after](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | Function | Yes |

## addBefore

```TypeScript
static addBefore(targetClass: Object, methodName: string, isStatic: boolean, before: Function): void
```

Inserts a function before a method of a class object. The inserted function is executed in prior to the original method of the class object.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | Object | Yes |
| methodName | string | Yes |
| [isStatic](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutinfo-depr-i.md) | boolean | Yes |
| before | Function | Yes |

## replace

```TypeScript
static replace(targetClass: Object, methodName: string, isStatic: boolean, instead: Function) : void
```

Replaces a method of a class object with another function. After the replacement, only the new function logic is executed. The final return value is the return value of the new function.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | Object | Yes |
| methodName | string | Yes |
| [isStatic](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutinfo-depr-i.md) | boolean | Yes |
| instead | Function | Yes |
