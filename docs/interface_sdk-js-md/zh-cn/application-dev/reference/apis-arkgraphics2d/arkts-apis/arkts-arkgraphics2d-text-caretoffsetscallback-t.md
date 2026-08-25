# CaretOffsetsCallback

```TypeScript
type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean
```

将文本行中每个字符的偏移量和索引值作为参数的回调方法。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |
| index | number | 是 |
| leadingEdge | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
