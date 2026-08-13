# PathIterator

Implements a path operation iterator. You can read path operation instructions by traversing the iterator. > **NOTE：**> > - The initial APIs of this class are supported since API version 18. > > - This module uses the physical pixel unit, px. > > - The module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

**Deprecated since:** -1

<!--Device-drawing-class PathIterator--><!--Device-drawing-class PathIterator-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor(path: Path)
```

Creates an iterator and binds it with a path.

**Since:** 23

**Deprecated since:** -1

<!--Device-PathIterator-constructor(path: Path)--><!--Device-PathIterator-constructor(path: Path)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes |

## hasNext

```TypeScript
hasNext(): boolean
```

Checks whether there is any next operation in the path operation iterator.

**Since:** 23

**Deprecated since:** -1

<!--Device-PathIterator-hasNext(): boolean--><!--Device-PathIterator-hasNext(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb
```

Retrieves the next operation in this path and moves the iterator to that operation.

**Since:** 18

**Deprecated since:** -1

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | Yes |
| offset | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb | undefined
```

Retrieves the next operation in this path and moves the iterator to that operation.

**Since:** 23

**Deprecated since:** -1

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | Yes |
| offset | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## peek

```TypeScript
peek(): PathIteratorVerb
```

Retrieves the next operation in this path, without moving the iterator.

**Since:** 18

**Deprecated since:** -1

<!--Device-PathIterator-peek(): PathIteratorVerb--><!--Device-PathIterator-peek(): PathIteratorVerb-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |

## peek

```TypeScript
peek(): PathIteratorVerb | undefined
```

Retrieves the next operation in this path, without moving the iterator.

**Since:** 23

**Deprecated since:** -1

<!--Device-PathIterator-peek(): PathIteratorVerb | undefined--><!--Device-PathIterator-peek(): PathIteratorVerb | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |
