# decodeURIComponent

## 导入模块

```TypeScript
```

## decodeURIComponent

```TypeScript
export function decodeURIComponent(uriComponent: string): string
```

decodeURIComponent()函数用于解码由 encodeURIComponent()或类似方法创建的 统一资源标识符（URI）组成部分。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function decodeURIComponent(uriComponent: string): string--><!--Device-unnamed-export function decodeURIComponent(uriComponent: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uriComponent | string | 是 | 需要解码的URI。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 解码后的URI组成部分。 |

