# Menu

The **Menu** component is a vertical list of items presented to the user.

> **NOTE** > > - This component is supported since API version 9. Newly added APIs will be marked with a superscript to indicate > their > > - The **Menu** component must be used together with the > [bindMenu](arkts-arkui-commonmethod-c.md#bindmenu) or > [bindContextMenu](arkts-arkui-commonmethod-c.md#bindcontextmenu) > method. It does not work when used alone.

## Child Components

This component contains the MenuItem and MenuItemGroup child components.

## Menu

```TypeScript
Menu()
```

Creates a fixed container for a menu. This API does not have any parameters.

> **NOTE：**
> 
> - Rules for calculating the width of menus and menu items:
> 
> 
> 
> - During the layout, the width of each menu item is expected to be the same. If a child component has its
> width set, the size calculation rule prevails.
> 
> 
> 
> - If no width is set for the **Menu** component, it applies a default two-column width to the **MenuItem**
> and **MenuItemGroup** child components. If a menu item's content area exceeds the two-column width, the
> **Menu** component automatically expands the menu item's content area.
> 
> 
> 
> - When an explicit width is set for the **Menu** component, its child components **MenuItem** and
> **MenuItemGroup** adopt a fixed width (equal to the **Menu** component's configured width minus the padding).
> 
> 
> 
> - The minimum width is 64 vp.
> 
> - Universal attributes unsupported by **Menu**: outline attributes and the
> shadow attribute

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Enums

| Name | Description |
| --- | --- |
| [SubMenuExpandingMode](arkts-arkui-submenuexpandingmode-e.md) | Enumerates the submenu expanding modes. |

## Examples

This example demonstrates how to implement a multi-level menu by configuring the builder parameter in MenuItem.

```TypeScript
@Entry
@Component
struct Index {
  @State select: boolean = true;
  // Replace $r('app.media.xxx') with the image resource file you use.
  private iconStr: ResourceStr = $r("app.media.view_list_filled");
  private iconStr2: ResourceStr = $r("app.media.arrow_right_filled");

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: "Copy", labelInfo: "Ctrl+C" })
      MenuItem({ content: "Paste", labelInfo: "Ctrl+V" })
    }
  }

  @Builder
  MyMenu(){
    Menu() {
      MenuItem({ startIcon: $r("app.media.icon"), content: "Menu item" })
      MenuItem({ startIcon: $r("app.media.icon"), content: "Menu item" })
        .enabled(false)
      MenuItem({
        startIcon: this.iconStr,
        content: "Menu item",
        endIcon: this.iconStr2,
        builder: ():void=>this.SubMenu()
      })
      MenuItemGroup({ header: 'Subtitle' }) {
        MenuItem({
          startIcon: this.iconStr,
          content: "Menu item",
          endIcon: this.iconStr2,
          builder: ():void=>this.SubMenu()
        })
        MenuItem({
          startIcon: $r("app.media.app_icon"),
          content: "Menu item",
          endIcon: this.iconStr2,
          builder: ():void=>this.SubMenu()
        })
      }
      MenuItem({
        startIcon: this.iconStr,
        content: "Menu item",
      })
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}
```

This example demonstrates how to implement a menu with symbol icons by configuring symbolStartIcon and symbolEndIcon.

```TypeScript
// xxx.ets
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic')).fontSize('24vp');
  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_trash')).fontSize('24vp');
  @State selectIconModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.checkmark')).fontSize('24vp');
  @State select: boolean = true;

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({ content: "Copy", labelInfo: "Ctrl+C" })
      MenuItem({ content: "Paste", labelInfo: "Ctrl+V" })
    }
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ symbolStartIcon: this.startIconModifier, content: "Menu item" })
      MenuItem({ symbolStartIcon: this.startIconModifier, content: "Menu item" })
        .enabled(false)
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Menu item",
        symbolEndIcon: this.endIconModifier,
        builder: (): void => this.SubMenu()
      })
      MenuItemGroup({ header: 'Subtitle' }) {
        MenuItem({
          symbolStartIcon: this.startIconModifier,
          content: "Menu item",
          symbolEndIcon: this.endIconModifier,
          builder: (): void => this.SubMenu()
        })
        MenuItem({
          symbolStartIcon: this.startIconModifier,
          content: "Menu item",
          symbolEndIcon: this.endIconModifier,
          builder: (): void => this.SubMenu()
        })
      }
      MenuItem({
        content: "Menu item",
      }).selected(this.select).selectIcon(this.selectIconModifier)
    }
  }

  build() {
    Row() {
      Column() {
        Text('click to show menu')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .bindMenu(this.MyMenu)
      .width('100%')
    }
    .height('100%')
  }
}
```

This example demonstrates how to configure the expand symbol color for menu submenus using subMenuExpandSymbol.

```TypeScript
import { SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State startIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_star'))
  @State endIconModifier: SymbolGlyphModifier = new SymbolGlyphModifier($r('sys.symbol.ohos_mic'))
  @State expandSymbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.chevron_down')).fontColor([Color.Red]).fontSize('24vp')

  @Builder
  SubMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Icons"
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "List"
      })
    }.backgroundColor(Color.Grey)
  }

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        symbolEndIcon: this.endIconModifier,
        content: "New folder",
        builder: (): void => this.SubMenu(),
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "Sort by",
        builder: (): void => this.SubMenu(),
      })
      MenuItem({
        symbolStartIcon: this.startIconModifier,
        content: "View mode",
        builder: (): void => this.SubMenu(),
      })
    }
    .subMenuExpandingMode(SubMenuExpandingMode.EMBEDDED_EXPAND)
    .backgroundColor(Color.Grey)
    .subMenuExpandSymbol(this.expandSymbolModifier)
  }

  build() {
    Button('click to show menu')
      .position({ top: 40, left: 40 })
      .bindMenu(this.MyMenu)
  }
}
```

This example demonstrates how to implement the divider style using menuItemGroupDivider.

```TypeScript
import { LengthMetrics } from '@kit.ArkUI'

@Entry
@Component
struct Index {

  @Builder
  MyMenu() {
    Menu() {
      MenuItem({ content: "Item Content" })
      MenuItem({ content: "Item Content" })
      MenuItem({ content: "Item Content" })
      MenuItemGroup() {
        MenuItem({ content: "Group Child" })
        MenuItem({ content: "Group Child" })
      }
      MenuItem({ content: "Item Content" })
    }
    .menuItemDivider({
      strokeWidth: LengthMetrics.vp(5),
      color: '#d5d5d5',
      mode: DividerMode.EMBEDDED_IN_MENU
    })
    .menuItemGroupDivider({
      strokeWidth: LengthMetrics.vp(5),
      color: '#707070',
      mode: DividerMode.EMBEDDED_IN_MENU
    })
  }

  build() {
    RelativeContainer() {
      Button("show menu")
        .bindMenu(this.MyMenu())
    }
    .height('100%')
    .width('100%')
  }
}
```
