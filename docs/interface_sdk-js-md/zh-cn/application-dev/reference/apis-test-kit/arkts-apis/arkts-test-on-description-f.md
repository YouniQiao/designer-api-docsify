# description

## description

```TypeScript
export function description(val: string, pattern?: MatchPattern): On
```

Specifies the description for the target Component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ON-export function description(val: string, pattern?: MatchPattern): On--><!--Device-ON-export function description(val: string, pattern?: MatchPattern): On-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | the description value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | 否 | the {@link MatchPattern} of description value,set it default {@link MatchPattern.EQUALS} if null or undefined. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

