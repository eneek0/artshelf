<script>
  document.querySelectorAll('.search-bar__filters-item').forEach(item ={" "}
  {item.addEventListener("click", function () {
    document
      .querySelectorAll(".search-bar__filters-item")
      .forEach((btn) => btn.classList.remove("active"));
    this.classList.add("active");
  })}
  ; );
</script>;
