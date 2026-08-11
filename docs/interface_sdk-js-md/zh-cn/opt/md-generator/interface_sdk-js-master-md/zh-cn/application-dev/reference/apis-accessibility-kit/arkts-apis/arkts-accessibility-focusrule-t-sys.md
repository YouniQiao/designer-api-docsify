# FocusRule（系统接口）

```TypeScript
export type FocusRule = 'bypassSelf' | 'bypassSelfDescendants' |
'checkSelf' | 'checkSelfBypassDescendants'
```

表示查找可聚焦节点时，如何判断起始节点及其子节点的聚焦能力。

**起始版本：** 23

<!--Device-unnamed-export type FocusRule = 'bypassSelf' | 'bypassSelfDescendants' |'checkSelf' | 'checkSelfBypassDescendants'--><!--Device-unnamed-export type FocusRule = 'bypassSelf' | 'bypassSelfDescendants' |'checkSelf' | 'checkSelfBypassDescendants'-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

| 类型 |
| --- |
| 'bypassSelf' |
| 'bypassSelfDescendants' |
| 'checkSelf' |
| 'checkSelfBypassDescendants' |
