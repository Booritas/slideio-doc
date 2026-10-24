# Categories and counting

A **category** (also called a classification) says what an annotation marks:
"Tumor", "Stroma", "Mitosis". Any annotation can have one category, set in the
[Annotation Properties pane](list-and-properties.md#annotation-properties-pane).
The category does not change how the annotation looks; set its colour
separately.

## Managing the category list

The viewer keeps one list of categories, shared by all slides. It starts as
**Tumor, Stroma, Necrosis, Normal, Artifact**.

To change it, open **Tools > Preferences...** and edit **Annotation
categories**, one per line. Blank lines, duplicates (ignoring case) and the
word "Unclassified" are dropped.

"Unclassified" is not a category: it means "no category". Typing it as a
classification clears the classification.

Category names are compared ignoring case and surrounding spaces, so "tumor"
and "Tumor " count as "Tumor".

## Counting with point markers

To count cells or structures:

1. Open the Annotation List ({kbd}`Ctrl+Shift+L`).
2. In **Counting:**, pick the category to count, or type a new one.
3. Choose the **Point Marker** tool ({kbd}`M`) and click each item.

Every marker you place gets the counting category, and the tally goes up by
one. Switch the counting category to count the next kind of item. A category
typed in **Counting:** is added to the category list when you place the first
marker with it.

Choose **(none)** to place markers without a category. The counting category
applies only to point markers; other shapes are drawn without a category.

To prevent accidental changes, the counting box ignores the arrow keys and the
mouse wheel unless its list is open.

## The tally

The tally under **Counting:** lists how many annotations carry each category:

1. every category in the list, in list order, including those at zero;
2. then categories found on annotations that are not in the list;
3. then **Unclassified**, if any annotation has no category.

The tally always covers the whole scene, including annotations on hidden
layers, whatever the list filter. Text, ruler and angle annotations are not
counted. When some counted annotations are on hidden layers, a note under the
tally says how many.

Export the tally with [File > Export Counts...](import-export.md#counts-csv).

## Renaming and removing categories

Right-click a category in the tally:

- **Rename...** renames the category in the list and on every annotation of
  this scene that carries it. Renaming onto an existing category merges the
  two. The change to the annotations is one undo step, "Rename Category"; the
  change to the list itself is not undone.
- **Remove from list** removes the category from the list. Annotations keep it,
  and it stays in the tally as a category not in the list.
