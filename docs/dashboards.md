# Dashboards

This file is a quick collections of useful links, tips, for dashboarding tools.
  

## Bokeh

- in notebook

    To render, you need to load the BokehJS library
    ```
    import bokeh.io
    bokeh.io.output_notebook()
    ```

    If the browser does not do that for you, you can ask bokeh to generate the necessary js for you when the function is called:
    ```
    from bokeh.resources import INLINE
    import bokeh.io
    bokeh.io.output_notebook(INLINE)
    ```


 
## Panel
  

Install with `pip install panel`. This should be enough for notebooks and scripts. 
  - To make panel work inside a VS code notebook, you will also need `jupyter_bokeh` [1]. Note that this is installed at the level of the jupyter server, it does not need to be added to your dependencies.


- Using sliders: it can be tricky to pass values into a function, see
https://medium.com/spatial-data-science/create-interactive-dashboards-with-panel-python-9ac13c84b227


From terminal:
- `panel serve --show --autoreload panel_app.py` serve the dashboard with autoreload, to speed up the development.

- `panel serve --show panel_app.py` 


#### Tips:
- It may happen that figures are plotted twice: use `%matplotlib agg` to avoid it!





## References

1. https://panel.holoviz.org/index.html

2. https://panel.holoviz.org/getting_started/index.html                 