# ModifierUtils

ModifierUtils provides utility methods for modifier and attribute operations.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-unnamed-export declare class ModifierUtils--><!--Device-unnamed-export declare class ModifierUtils-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## isInstanceOf

```TypeScript
static isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean
```

Checks if the given instance is of the specified component type.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ModifierUtils-static isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean--><!--Device-ModifierUtils-static isInstanceOf<T extends CommonMethod<T>>(instance: T, componentName: string): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | T | 是 | The instance to check. |
| componentName | string | 是 | The name of the component type to check against. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the instance is of the specified component type. Otherwise, returns false. |

