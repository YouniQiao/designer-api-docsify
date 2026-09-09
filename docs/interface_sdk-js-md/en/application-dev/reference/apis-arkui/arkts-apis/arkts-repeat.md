# repeat(Defines Repeat component.)

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md) | In addition to the drag-and-drop sorting attribute, the following attributes are supported. |

### Interfaces

| Name | Description |
| --- | --- |
| [RepeatItem](arkts-arkui-repeatitem-i.md) | Construct a new type for each item. |
| [TemplateOptions](arkts-arkui-templateoptions-i.md) | When **cachedCount** is set to the maximum number of nodes in the display area of the container component for the current template, **Repeat** achieves maximum reuse efficiency. If there are no nodes of the current template in the container component's display area, the cache list is not released, which increases application memory usage. You are advised to set **cachedCount** to the number of nodes within the container component's display area and adjust the value according to the actual situation. Yet, setting **cachedCount** to less than 2 is not recommended, as this may lead to the frequent node creation during rapid scrolling and result in performance degradation. |
| [VirtualScrollOptions](arkts-arkui-virtualscrolloptions-i.md) | Configures the expected total number of data items to be loaded in lazy loading mode, the reuse capability, and the precise data lazy loading capability. |

### Enums

| Name | Description |
| --- | --- |
| [RepeatMemOptStrategy](arkts-arkui-repeatmemoptstrategy-e.md) | Defines a type for memory optimization strategy. |

### Types

| Name | Description |
| --- | --- |
| [RepeatArray](arkts-arkui-repeatarray-t.md) | Defines a union type for **Repeat** data source parameters. |
| [RepeatInterface](arkts-arkui-repeatinterface-t.md) | Indicates the type of Repeat. |
| [RepeatItemBuilder](arkts-arkui-repeatitembuilder-t.md) | Defines builder function to render one template type. |
| [TemplateTypedFunc](arkts-arkui-templatetypedfunc-t.md) | Function that returns typed string to render one template. |

### Constants

| Name | Description |
| --- | --- |
| [Repeat](arkts-arkui-repeat-con.md) | Defines Repeat Component, and Add More Array Type. |

## Examples

In the following example, the automatic memory optimization strategy is used through the memoryOptimizationStrategy attribute of [VirtualScrollOptions](arkts-arkui-virtualscrolloptions-i.md). Click the Scroll button to make the list jump, and the old nodes enter the cache pool. When the application goes to the background, the cache is cleared. When the application returns to the foreground, the cache is restored.
Since API version 26.0.0, VirtualScrollOptions adds the memoryOptimizationStrategy attribute.

```TypeScript
@ComponentV2
struct ChildComponent {
  aboutToAppear() {
    console.info('ChildComponent aboutToAppear');
  }
  aboutToDisappear() {
    console.info('ChildComponent aboutToDisappear');
  }
  build() {
    Text('ChildComponent')
  }
}

@Entry
@ComponentV2
struct MemoryOptimizeDemo {
  @Local data: Array<number> = [];
  private scroller: Scroller = new Scroller();
  aboutToAppear() {
    for (let i = 0; i < 100; i++) {
      this.data.push(i);
    }
  }
  build() {
    Column() {
      Button('Scroll').onClick(() => { // Click the button to trigger list scrolling, and the old components enter the cache pool.
        this.scroller.scrollToIndex(30);
      })
      List({ scroller: this.scroller }) {
        Repeat<number>(this.data)
          .each((repeatItem: RepeatItem<number>) => {
            ListItem() {
              ChildComponent()
            }
          })
          .virtualScroll({ memoryOptimizationStrategy: RepeatMemOptStrategy.ENABLE_AUTO_CACHE_OPTIMIZATION }) // Use the automatic memory optimization strategy.
      }
      .cachedCount(5)
    }
  }
}
```
