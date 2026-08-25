# Aspect

提供支持面向切面编程（AOP）的 API。这些 API 可用于对类方法进行插桩或替换。

**起始版本：** 11

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## addAfter

```TypeScript
static addAfter(targetClass: Object, methodName: string, isStatic: boolean, after: Function): void
```

在类对象的方法后插入一个函数。最终的返回值为被插入函数的返回值。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | Object | 是 |
| methodName | string | 是 |
| [isStatic](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutinfo-depr-i.md) | boolean | 是 |
| [after](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | Function | 是 |

## addBefore

```TypeScript
static addBefore(targetClass: Object, methodName: string, isStatic: boolean, before: Function): void
```

在类对象的方法前插入一个函数。被插入的函数会先于类对象的原方法执行。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | Object | 是 |
| methodName | string | 是 |
| [isStatic](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutinfo-depr-i.md) | boolean | 是 |
| before | Function | 是 |

## replace

```TypeScript
static replace(targetClass: Object, methodName: string, isStatic: boolean, instead: Function) : void
```

使用另一个函数替换类对象的方法。替换后，仅执行新函数的逻辑。最终的返回值为新函数的返回值。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | Object | 是 |
| methodName | string | 是 |
| [isStatic](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutinfo-depr-i.md) | boolean | 是 |
| instead | Function | 是 |
