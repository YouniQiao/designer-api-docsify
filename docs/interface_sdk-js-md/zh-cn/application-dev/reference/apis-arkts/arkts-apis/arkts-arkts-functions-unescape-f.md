# unescape

## unescape

```TypeScript
export function unescape(str: string): string
```

This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the compatibility table at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.unescape() is a non-standard function implemented by browsers and was only standardized for cross-engine compatibility. It is not required to be implemented by all JavaScript engines and may not work everywhere. Use decodeURIComponent() or decodeURI() if possible.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export function unescape(str: string): string--><!--Device-unnamed-export function unescape(str: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| str | string | 是 | a string to be decoded |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a new string in which hexadecimal escape sequences are replaced with the characters that they represent. |

