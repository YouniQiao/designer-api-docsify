# PathIteratorVerb

迭代器包含的路径操作类型枚举，可用于读取path的操作指令。常用于路径分析、路径转换、路径动画等需要解析路径构成的场景。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-drawing-enum PathIteratorVerb--><!--Device-drawing-enum PathIteratorVerb-End-->

**System capability:** SystemCapability.Graphics.Drawing

## MOVE

```TypeScript
MOVE = 0
```

设置起始点。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-MOVE = 0--><!--Device-PathIteratorVerb-MOVE = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## LINE

```TypeScript
LINE = 1
```

添加线段。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-LINE = 1--><!--Device-PathIteratorVerb-LINE = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## QUAD

```TypeScript
QUAD = 2
```

添加二阶贝塞尔圆滑曲线。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-QUAD = 2--><!--Device-PathIteratorVerb-QUAD = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

## CONIC

```TypeScript
CONIC = 3
```

添加圆锥曲线。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-CONIC = 3--><!--Device-PathIteratorVerb-CONIC = 3-End-->

**System capability:** SystemCapability.Graphics.Drawing

## CUBIC

```TypeScript
CUBIC = 4
```

添加三阶贝塞尔圆滑曲线。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-CUBIC = 4--><!--Device-PathIteratorVerb-CUBIC = 4-End-->

**System capability:** SystemCapability.Graphics.Drawing

## CLOSE

```TypeScript
CLOSE = 5
```

路径闭合。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-CLOSE = 5--><!--Device-PathIteratorVerb-CLOSE = 5-End-->

**System capability:** SystemCapability.Graphics.Drawing

## DONE

```TypeScript
DONE = CLOSE + 1
```

路径设置完成。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PathIteratorVerb-DONE = CLOSE + 1--><!--Device-PathIteratorVerb-DONE = CLOSE + 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

