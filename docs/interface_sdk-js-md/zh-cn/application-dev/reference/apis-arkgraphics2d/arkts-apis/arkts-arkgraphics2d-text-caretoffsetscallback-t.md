# CaretOffsetsCallback

```TypeScript
type CaretOffsetsCallback = (offset: double, index: int, leadingEdge: boolean) => boolean
```

将文本行中每个字符的偏移量和索引值作为参数的回调方法。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：double | 是 |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| leadingEdge | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
